from typing import Dict, Any
from django.contrib import messages
from django.core.exceptions import SuspiciousOperation
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from decimal import Decimal
from rewards.models import Reward, UserPoints


SESSION_KEY_POINTS_GRANTED = 'points_granted'
SESSION_KEY_POINTS_SPENT = 'points_spent'
GUEST_POINTS = 10
ADD_POINTS_BONUS = 5


def get_points(user, session):
    if user.is_authenticated:
        user_points, _ = UserPoints.objects.get_or_create(user=user)
        return user_points.points_granted, user_points.points_spent
    else:
        return Decimal(session.get(SESSION_KEY_POINTS_GRANTED, default=GUEST_POINTS)), \
            Decimal(session.get(SESSION_KEY_POINTS_SPENT, default='0'))


class RewardsListView(generic.ListView):
    template_name = 'rewards/list.html'
    context_object_name = 'rewards'

    def get_queryset(self):
        return Reward.objects.all()

    def get_context_data(self, **kwargs: object) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        points_avail, points_spent = get_points(self.request.user, self.request.session)
        context['redeemable_points'] = points_avail - points_spent
        return context


class RewardsClaimView(generic.View):
    template_name = 'rewards/claim.html'

    def post(self, request):
        claimed_reward_ids = request.POST.getlist('rewardId')
        claimed_rewards = Reward.objects.filter(id__in=claimed_reward_ids)
        point_sum = claimed_rewards.aggregate(Sum('point_value')).get('point_value__sum', 0.00)
        points_granted, points_spent = get_points(request.user, request.session)

        if point_sum <= points_granted - points_spent:
            messages.add_message(
                request, messages.INFO,
                f"You successfully claimed the following rewards: {', '.join([r.name for r in claimed_rewards])}"
            )

            if request.user.is_authenticated:
                user_points, _ = UserPoints.objects.get_or_create(user=request.user)
                user_points.points_spent += point_sum
                user_points.save()
            else:
                request.session[SESSION_KEY_POINTS_SPENT] = str(point_sum + points_spent)

            return redirect(reverse('rewards:list'))

        else:
            raise SuspiciousOperation("Invalid request; Exceeded available points")


class RewardsBonusView(generic.View):

    def post(self, request):
        num_points = Decimal(request.POST.get('numPoints', ADD_POINTS_BONUS))
        if request.user.is_authenticated:
            user_points, _ = UserPoints.objects.get_or_create(user=request.user)
            user_points.points_granted += num_points
            user_points.save()
            points_granted = user_points.points_granted
        else:
            points_granted = num_points + Decimal(request.session.get(SESSION_KEY_POINTS_GRANTED, default='0'))
            request.session[SESSION_KEY_POINTS_GRANTED] = str(points_granted)
        return JsonResponse({
            'status': 'ok',
            'pointsAdded': float(num_points),
            'pointsGranted': float(points_granted)
        })

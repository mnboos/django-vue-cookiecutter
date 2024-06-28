import {computed, inject, ref} from 'vue'
import {defineStore} from 'pinia'

export const useRewardStore = defineStore('reward', () => {

        const pointsRedeemed = ref(0);
        const pointsAvailable = ref(0);
        const rewardsRedeemed = ref({});
        const submitInProgress = ref(false);

        const addPointsUrl = inject('addPointsUrl')
        const csrfToken = inject('csrfToken')

        function redeem(rewardId, points) {
            rewardsRedeemed.value[rewardId] = true;
            pointsRedeemed.value += points;
        }

        function unRedeem(rewardId, points) {
            rewardsRedeemed.value[rewardId] = false;
            pointsRedeemed.value -= points;
        }

        function isRedeemed(rewardId) {
            return rewardsRedeemed.value[rewardId] ?? false;
        }

        async function addPoints(numPoints) {
            try {
                const response = await fetch(addPointsUrl, {
                    method: 'POST',
                    headers: {
                        "X-CSRFToken": csrfToken,
                        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
                    },
                    body: `numPoints=${numPoints}`
                });
                const responseJson = await response.json();
                pointsAvailable.value += responseJson['pointsAdded'];
            } catch (e) {
                // TODO: handle correctly
                console.log(e);
            }
        }

        function reset() {
            rewardsRedeemed.value = {};
            pointsRedeemed.value = 0;
        }

        const redeemedIds = computed(
            () => Object.entries(rewardsRedeemed.value)
                .filter(([_, value]) => value)
                .map((e) => e[0])
        )

        return {
            pointsRedeemed, pointsAvailable, rewardsRedeemed, submitInProgress,
            redeem, unRedeem,
            isRedeemed, redeemedIds,
            addPoints, reset
        }
    },
    {persist: true}
)

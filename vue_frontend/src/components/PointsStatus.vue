<script setup>
import {computed, inject, ref, watch} from 'vue'
import {useRewardStore} from "@/stores/reward";

defineOptions({ name: 'PointsStatus' })
const props = defineProps({
  pointsAvailable: {
    type: Number,
    required: true,
  },
  claimUrl: {
    type: String,
    required: true,
  },
})

const csrfToken = inject('csrfToken')
const addPointsUrl = inject('addPointsUrl');

const rewardStore = useRewardStore()
const currentSelection = ref(rewardStore.redeemedIds);
rewardStore.pointsAvailable = props.pointsAvailable; // set initial available points
rewardStore.submitInProgress = false; // set submission status to false

const remainingPoints = computed(() => {
  return rewardStore.pointsAvailable - rewardStore.pointsRedeemed;
})

function beforeSubmit(evt) {
  rewardStore.submitInProgress = true;
  rewardStore.reset();
}

watch(() => rewardStore.redeemedIds, async (redeemed, _) => {
  if (!rewardStore.submitInProgress) {
    currentSelection.value = redeemed;
  }
})

</script>

<template>
  <div class="container" v-html="$djangoSlots.message"></div>
  <div class="container" v-show="!rewardStore.submitInProgress">
    <div class="row justify-content-around">
      <div class="col-4 text-center card bg-light p-0 h5">
        <div class="card-header">Points Redeemed</div>
        <div class="card-body">{{ rewardStore.pointsRedeemed }}</div>
      </div>
      <div class="col-4 text-center card bg-light p-0 h5">
        <div class="card-header">Points Remaining</div>
        <div class="card-body" :class="{ 'text-danger': remainingPoints < 0 }">
          {{ remainingPoints }}
        </div>
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col text-center mt-5">

        <!-- An example of using vue to directly submit a form to a Django view -->
        <form @submit="beforeSubmit" method="post" :action="claimUrl" v-show="!rewardStore.submitInProgress">
          <input type="hidden" name="csrfmiddlewaretoken" :value="csrfToken">
          <template v-for="rewardId in currentSelection">
            <input type="hidden" name="rewardId" :value="rewardId">
          </template>
          <button class="btn btn-success btn-lg"
                  :disabled="rewardStore.pointsRedeemed <= 0 || remainingPoints < 0"
          >Claim my rewards
          </button>
        </form>

        <div v-show="rewardStore.submitInProgress" style="height: 42px" class="text-center">
          <span class="spinner-grow" role="status"></span>
        </div>
      </div>
    </div>
  </div>
  <div v-show="rewardStore.submitInProgress" style="height: 120px" class="text-center">
    <span class="spinner-grow m-5" role="status"></span>
  </div>
  <Teleport to="footer">
    <div class="container" v-html="$djangoSlots.disclaimer"></div>
  </Teleport>
  <Teleport to="#alerts">
    <div class="alert mb-0" role="alert"
         :class="{ 'alert-danger': remainingPoints < 4, 'alert-light': remainingPoints >= 4 }">
      <b>Need more points?</b>
      Earn bonus points: <a href="#" class="link-dark" @click="rewardStore.addPoints(5)">+5</a>
      &nbsp;<a href="#" class="link-dark" @click="rewardStore.addPoints(15)">+15</a>
      <span v-if="remainingPoints > 0" class="float-end">
        <b>Had Enough?</b>
        &nbsp;<a href="#" class="link-dark x-float-end" @click="rewardStore.addPoints(-1 * remainingPoints)">forfeit all
        points</a>
      </span>
    </div>
  </Teleport>
</template>
<style scoped>
/* Scoped styles will apply only to this component */
button[disabled] {
  background: #ccc;
  border-color: #aaa;
  color: #999;
}
</style>



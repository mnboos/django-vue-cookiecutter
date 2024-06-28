<script setup>
import {useRewardStore} from "@/stores/reward";

defineOptions({ name: 'RewardClaim' })
defineProps({
  rewardId: {
    type: String,
    required: true
  },
  points: {
    type: Number,
    required: true,
  }
})

const rewardStore = useRewardStore()

</script>

<template>
  <div>
    <a v-if="!rewardStore.isRedeemed(rewardId)"
       @click="rewardStore.redeem(rewardId, points)"
       class="btn btn-light">Redeem this Reward</a>
    <a v-else
       @click="rewardStore.unRedeem(rewardId, points)"
       class="btn text-light btn-outline-dark">Un-redeem</a>
  </div>
</template>

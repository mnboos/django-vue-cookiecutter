import {createApp} from 'vue'
import {createPinia} from 'pinia'
import DjangoUtilsPlugin from 'vue-plugin-django-utils'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import {convertDatasetToProps} from 'vue-plugin-django-utils'

import RewardClaim from "@/components/RewardClaim.vue";
import PointsStatus from "@/components/PointsStatus.vue";

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)


const statusEl = document.getElementById('points-status')
if (statusEl) {
  const app = createApp(PointsStatus, convertDatasetToProps({
    dataset: {...statusEl.dataset},
    component: PointsStatus
  }))
  app.use(pinia)
  app.use(DjangoUtilsPlugin, {rootElement: statusEl})
  app.mount(statusEl)
}

document.querySelectorAll('.reward-claim').forEach(el => {
      const app = createApp(RewardClaim, convertDatasetToProps({
        dataset: {...el.dataset},
        component: RewardClaim
      }))
      app.use(pinia)
      app.use(DjangoUtilsPlugin, {rootElement: el})
      app.mount(el)
    }
);

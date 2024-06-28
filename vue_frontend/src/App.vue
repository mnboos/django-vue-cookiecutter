<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import IconVue from "@/components/icons/IconVue.vue";
</script>

<template>
  <header>
    <IconVue class="logo" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
      <hr style="height: 1rem;"/>
      <div>For more Vue integration tips and techniques, check out <b>Vue Demo</b> from the navigation menu above.</div>
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>

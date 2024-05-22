<template>
  <div>
    <div>
      <img src="@/assets/landing001.png" alt="" :class="['landing-title', { 'fade-in': visible }]">
    </div>

    <div ref="target">
      <img src="@/assets/landing002.png" alt="" :class="['landing-semi-title', { 'inMonitor' : targetIsVisible }]" style="margin-bottom:200px;">
    </div>
    
    <div ref="target2">
      <img src="@/assets/landing003.png" alt="" :class="['landing-service01', {' inMonitor' : targetIsVisible2}]" style="margin-bottom:200px;">
    </div>

    <div ref="target3">
    <img src="@/assets/landing004.png" alt="" :class="['landing-service02', {' inMonitor' : targetIsVisible3}]" style="margin-bottom:200px;">
    </div>

    <div ref="target4">
    <img src="@/assets/landing005.png" alt="" :class="['landing-service03', {' inMonitor' : targetIsVisible4}]" style="margin-bottom:200px;">
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useIntersectionObserver } from  '@vueuse/core'

const target = ref(null)
const target2 = ref(null)
const target3 = ref(null)
const target4 = ref(null)


const targetIsVisible = ref(false)
const targetIsVisible2 = ref(false)
const targetIsVisible3 = ref(false)
const targetIsVisible4 = ref(false)

const visible = ref(false)

useIntersectionObserver(target, ([{isIntersecting}]) => {
  targetIsVisible.value = isIntersecting
},
)

useIntersectionObserver(target2, ([{isIntersecting}]) => {
  targetIsVisible2.value = isIntersecting
},
)

useIntersectionObserver(target3, ([{isIntersecting}]) => {
  targetIsVisible3.value = isIntersecting
},
)

useIntersectionObserver(target4, ([{isIntersecting}]) => {
  targetIsVisible4.value = isIntersecting
},
)


onMounted(() => {

  setTimeout(() => {
    visible.value = true;
  }, 200)
})

</script>

<style scoped>
.landing-title {
  opacity: 0;
  transition: opacity 1s ease-in-out;
}

.landing-title.fade-in {
  opacity: 1;
}

.landing-semi-title {
  opacity: 0;
  transition: opacity 0.8s ease-in-out;
}
.landing-service01 {
  opacity: 0;
  transition: opacity 0.8s ease-in-out;
}
.landing-service02 {
  opacity: 0;
  transition: opacity 0.8s ease-in-out;
}
.landing-service03 {
  opacity: 0;
  transition: opacity 0.8s ease-in-out;
}

.inMonitor {
  opacity : 1;
}
</style>

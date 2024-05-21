<template>
    <h1>펫보험</h1>
    <div v-for="insurance in store.insurances" :key="insurance.id">
    </div>
</template>

<script setup>
import { useDepositStore } from '@/stores/deposit';
import { onMounted } from 'vue'
const store = useDepositStore()

onMounted(() => {
    store.getInsurance()
})


</script>

<style scoped>

</style>
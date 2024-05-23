<template>
    <div class="intro">
        <!-- 인트로 작성 -->
        <RouterLink :to="{ name: 'DepositView' }" >
            <img src="@/assets/bank_intro.png" alt="" class="select-img">
        </RouterLink>
        <RouterLink :to="{ name: 'InsuranceView' }">
            <img src="@/assets/insurance_intro.png" alt="" class="select-img">
        </RouterLink>
    </div>
</template>

<script>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.intro {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: row;
    width: 100%;
    height: 100vh;
    /* padding-top: 100px; */
}

.select-img {
    width: 1000px;
    margin: 0;
    opacity: 1;
}

.select-img:hover {
    transform: translateY(-50px);
    opacity: 0.3;
    transition: all 0.7s ease-in-out;
}
</style>
<template>
  <div class="random">
    <h1 class="text-center"><b>Random</b></h1>
    <div class="balls mx-auto text-white font-bold">
      <div class="text-center fw-bold"><span style="font-size:x-large">P</span></div>
      <div class="text-center fw-bold"><span style="font-size:x-large">I</span></div>
      <div class="text-center fw-bold"><span style="font-size:x-large">C</span></div>
      <div class="text-center fw-bold"><span style="font-size:x-large">K</span></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RandomView",
};
</script>

<style scoped>
.balls {
  width: 3.5em;
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
  justify-content: space-between;
}

.balls div {
  width: 0.8em;
  height: 0.8em;
  border-radius: 50%;
  background-color: #fc2f70;
  transform: translateY(-100%);
  animation: wave 0.8s ease-in-out alternate infinite;
}

.balls div:nth-of-type(1) {
  animation-delay: -0.4s;
}

.balls div:nth-of-type(2) {
  animation-delay: -0.2s;
}

@keyframes wave {
  from {
    transform: translateY(-100%);
  }
  to {
    transform: translateY(100%);
  }
}
</style>

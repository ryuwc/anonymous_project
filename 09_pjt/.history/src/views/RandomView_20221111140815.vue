<template>
  <div class="random">
    <h1 class="text-center"><b>Random</b></h1>
    <div class="balls mx-auto">
      <div>P</div>
      <div>I</div>
      <div>C</div>
      <div>K</div>
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
  width: 4em;
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
  justify-content: space-between;
}

.balls div {
  width: 2em;
  height: 2em;
  border-radius: 50%;
  background-color: #fc2f70;
}

.balls div:nth-of-type(1) {
  transform: translateX(-150%);
  /* animation: left-swing 0.5s ease-in alternate infinite; */
}
.balls div:nth-of-type(2) {
  transform: translateX(-100%);
  /* animation: left-swing 0.5s ease-in alternate infinite; */
}
.balls div:nth-of-type(3) {
  transform: translateX(-100%);
  /* animation: right-swing 0.5s ease-in alternate infinite; */
}

.balls div:nth-of-type(4) {
  transform: translateX(-95%);
  /* animation: right-swing 0.5s ease-out alternate infinite; */
}

@keyframes left-swing {
  50%,
  100% {
    transform: translateX(95%);
  }
}

@keyframes right-swing {
  50% {
    transform: translateX(-95%);
  }
  100% {
    transform: translateX(100%);
  }
}
</style>

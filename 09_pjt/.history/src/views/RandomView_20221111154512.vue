<template>
  <div class="random">
    <br>
      <div class="text-box"
      style="margin-left: 45vw;"
      >
      <a href="#" 
      class="btn btn-white btn-animate"
       style="border: solid 1px black"
       @click="pickMovie"
       >click me</a>
    </div>

    <div class="balls text-white font-bold"
    style="margin-left: 45vw; margin-top: 110px;"
    >
      <div class="text-center fw-bold"><span style="font-size:x-large">P</span></div>
      <div class="text-center fw-bold"><span style="font-size:x-large">I</span></div>
      <div class="text-center fw-bold"><span style="font-size:x-large">C</span></div>
      <div class="text-center fw-bold"><span style="font-size:x-large">K</span></div>
    </div>
    <br>
    <br>
    <br>
    <div v-if="movie" class="mx-auto">
      <MovieCard
      :movie="movie"
      />
    </div>
    
  </div>
</template>

<script>
import _ from 'lodash'
import MovieCard from '@/components/MovieCard.vue';


export default {
  name: "RandomView",
  data() {
    return {
      movie: null  
    }
  },
  components:{
    MovieCard,
  },
  methods: {
    pickMovie() {
      const randomMovie = _.sample(this.$store.state.movies)
      console.log(randomMovie.title)
      this.movie = randomMovie
    }
  },
  computed: {
  }
};
</script>

<style scoped>
.balls {
  width: 10em;
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
  justify-content: space-between;
}

.balls div {
  width: 3em;
  height: 3em;
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
.balls div:nth-of-type(3) {
  animation-delay: -0.1s;
}

@keyframes wave {
  from {
    transform: translateY(-50%);
  }
  to {
    transform: translateY(50%);
  }
}
.text-box{
  margin-left: 0vw;
}


.btn:link,
.btn:visited {
    text-transform: uppercase;
    text-decoration: none;
    padding: 15px 40px;
    display: inline-block;
    border-radius: 100px;
    transition: all .2s;
    position: absolute;
}

.btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.btn:active {
    transform: translateY(-1px);
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}

.btn-white {
    background-color: #fff;
    color: #777;
}

.btn::after {
    content: "";
    display: inline-block;
    height: 100%;
    width: 100%;
    border-radius: 100px;
    position: absolute;
    top: 0;
    left: 0;
    z-index: -1;
    transition: all .4s;
}

.btn-white::after {
    background-color: #fff;
}

.btn:hover::after {
    transform: scaleX(1.4) scaleY(1.6);
    opacity: 0;
}

.btn-animated {
    animation: moveInBottom 5s ease-out;
    animation-fill-mode: backwards;
}

@keyframes moveInBottom {
    0% {
        opacity: 0;
        transform: translateY(30px);
    }

    100% {
        opacity: 1;
        transform: translateY(0px);
    }
}
</style>

import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: null
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, sendData) {
      state.movies = sendData
      // console.log(state.movies)
    }
  },
  actions: {
    getMovies(context) {
      
      axios({
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params: {
          api_key: '7f1cec35eda90e95bd4840f197f3186c'
        },
      })
      .then((res) => {
        const sendData = res.data.results
        // console.log(typeof(sendData));
        context.commit('GET_MOVIES', sendData)
      })
      .catch((err => console.log(err)))
    }
  },
  modules: {
  }
})

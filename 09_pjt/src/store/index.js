import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: null,
    wantMovies: [],
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, sendData) {
      state.movies = sendData
      // console.log(state.movies)
    },
    CREATE_WANT_MOVIE(state, newWantMovie) {
      state.wantMovies.push(newWantMovie)
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
    },
    createWantMovie(context, wantMovie) {
      const newWantMovie = {
        title: wantMovie,
        isCompleted: false,
      }
      context.commit('CREATE_WANT_MOVIE', newWantMovie)
    }
  },
  modules: {
  }
})

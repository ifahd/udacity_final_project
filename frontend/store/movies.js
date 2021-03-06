const state = () => ({
  movies: [],
  movie: {},
})

const getters = {
  movies (state) {
    return state.movies
  },
  movie (state) {
    return state.movie
  }
}

const mutations = {
  movies (state, payload) {
    state.movies = payload
  },
  movie (state, payload) {
    state.movie = payload
  }
}

const actions = {
  all (context) {
    this.$axios.$get('/movies')
      .then((res) => {
        context.commit('movies', res.movies)
      })
  },
  get (context, id) {
    this.$axios.$get('/movies/' + id)
      .then((res) => {
        context.commit('movie', res.movie)
      })
  },
  create (context, payload) {
    return new Promise((resolve, reject) => {
      this.$axios.$post('/movies', payload)
        .then((res) => {
          resolve(res)
        })
        .catch((error) => {
          console.log(error)
        })
    })
  },
  update (context, payload) {
    return new Promise((resolve, reject) => {
      this.$axios.$patch('/movies/' + payload.id, payload)
        .then((res) => {
          resolve(res)
        })
        .catch((error) => {
          console.log(error)
        })
    })
  }
}
export default {
  state,
  getters,
  mutations,
  actions
}

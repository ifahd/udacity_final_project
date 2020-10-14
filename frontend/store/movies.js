const state = () => ({
  movies: []
})

const getters = {
  movies (state) {
    return state.movies
  }
}

const mutations = {
  movies (state, payload) {
    state.movies = payload
  }
}

const actions = {
  all (context) {
    this.$axios.$get('/movies')
      .then((res) => {
        context.commit('movies', res.movies)
      })
  },
  new (context, payload) {
    return new Promise((resolve, reject) => {
      this.$axios.$post('/movies', payload)
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

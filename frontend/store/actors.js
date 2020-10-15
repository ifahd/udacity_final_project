const state = () => ({
  actors: [],
  actor: {},
})

const getters = {
  actors (state) {
    return state.actors
  },
  actor (state) {
    return state.actor
  }
}

const mutations = {
  actors (state, payload) {
    state.actors = payload
  },
  actor (state, payload) {
    state.actor = payload
  }
}

const actions = {
  all (context) {
    this.$axios.$get('/actors')
      .then((res) => {
        context.commit('actors', res.actors)
      })
  },
  get (context, id) {
    this.$axios.$get('/actors/' + id)
      .then((res) => {
        context.commit('actor', res.actor)
      })
  },
  create (context, payload) {
    return new Promise((resolve, reject) => {
      this.$axios.$post('/actors', payload)
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
      this.$axios.$patch('/actors/' + payload.id, payload)
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

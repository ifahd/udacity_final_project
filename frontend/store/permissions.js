export const state = () => ({
  permissions: []
})

export const getters = {
  permissions (state) {
    return state.permissions
  }
}

export const mutations = {
  setPermissions (state, permissions) {
    state.permissions = permissions
  }
}

export const actions = {
  setPermissions ({ commit }, permissions) {
    commit('setPermissions', permissions)
  },
}

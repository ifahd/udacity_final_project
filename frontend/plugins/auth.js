export default function ({ app, $auth, env }) {
  if ($auth.loggedIn) {
    app.$axios.$get(app.$axios.defaults.baseURL + '/permissions')
    .then((response) => {
      app.store.dispatch('permissions/setPermissions',response.permissions)
    })
  }
}

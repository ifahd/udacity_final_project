export default function ({ app, $auth, env }) {
  if ($auth.loggedIn) {
    app.$axios.$get('http://127.0.0.1:5000/permissions')
    .then((response) => {
      // app.store.commit('permissions', response.permissions)
      app.store.dispatch('permissions/setPermissions',response.permissions)
      console.log(app.store.getters['permissions/permissions']);
    })
    // if(app.store.getters.permissions.length == 0) {
    // }
    // app.$axios.$get('https://' + env.AUTH0_DOMAIN + '/.well-known/jwks.json')
  }
}
// https://{AUTH0_DOMAIN}/.well-known/jwks.json
// process.env.AUTH0_DOMAIN

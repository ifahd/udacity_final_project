<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="/">Casting Agency</b-navbar-brand>
        <b-navbar-nav>
          <template v-if="$auth.loggedIn">
            <b-nav-item href="/movies">Movies</b-nav-item>
            <b-nav-item href="/actors">Actors</b-nav-item>
            <b-nav-item href="/logout" class="ml-2">Logout</b-nav-item>
          </template>
          <template v-else>
            <b-nav-item href="/login" class="ml-2">Login</b-nav-item>
          </template>
        </b-navbar-nav>
    </b-navbar>
    <Nuxt :permissions="permissions"/>
  </div>
</template>
<script>
export default {
  computed: {
    permissions() {
      return this.$store.getters.permissions
    }
  },
}
</script>
<style>
html {
  font-family:
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}

.button--green {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
}

.button--green:hover {
  color: #fff;
  background-color: #3b8070;
}

.button--grey {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #35495e;
  color: #35495e;
  text-decoration: none;
  padding: 10px 30px;
  margin-left: 15px;
}

.button--grey:hover {
  color: #fff;
  background-color: #35495e;
}
</style>

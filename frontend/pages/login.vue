<template>
  <p>Signing in...</p>
</template>
<script>
export default {
  created() {
    this.$auth.loginWith('auth0')
  }
}
</script>

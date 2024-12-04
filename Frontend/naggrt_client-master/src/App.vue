<template>
  <v-app>
    <v-app-bar app color="secondary" dark>
      <div class="d-flex align-center">
        <router-link to="/">
          <v-btn href="https://github.com/j-rayx" target="_blank" text>
            <v-icon>mdi-message-text</v-icon>
            <span class="mr-2">Naggrt</span>
          </v-btn>
        </router-link>
      </div>
      <v-spacer></v-spacer>
      <router-link :to="{ name: 'event-list' }">
        <h6 class="nav-link">Events</h6>
      </router-link>
      <router-link :to="{ name: 'poster-account', params: { id: '2' } }">
        <h6 class="nav-link">Account</h6>
      </router-link>
    </v-app-bar>

    <v-main align="center" justify="center">
      <router-view />
      <!-- <EventList /> -->
    </v-main>
  </v-app>
</template>

<script>
// import EventCard from "./components/EventCard";
//import Carousel from "./components/Carousel";
//import EventList from "./views/EventList";

export default {
  name: "App",

  components: {
    // EventCard,
    //Carousel,
    //EventList
  },

  data: () => ({
    //
  })
};
</script>
<style scoped>
.nav-link {
  text-decoration: none;
  color: aliceblue;
  font-family: "Montserrat", sans-serif;
}
</style>

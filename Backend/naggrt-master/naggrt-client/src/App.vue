<template>
  <v-app>
    <v-app-bar app color="secondary" dark>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn href="https://github.com/j-rayx" target="_blank" text>
        <span class="mr-2">Naggrt</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <EventList />

      <!-- <EventCard />-->
    </v-content>
  </v-app>
</template>

<script>
// import EventCard from "./components/EventCard";
//import Carousel from "./components/Carousel";
import EventList from "./views/EventList";

export default {
  name: "App",

  components: {
    // EventCard,
    //Carousel,
    EventList
  },

  data: () => ({
    //
  })
};
</script>

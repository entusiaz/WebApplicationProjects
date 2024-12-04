<template>
  <div class="home container-fluid h-100">
    <div class="row">
      <v-row align="center" justify="center">
        <div class="col-md-4">
          <Carousel />
          <EventCard v-for="event in events" :key="event.id" :event="event" />
        </div>
      </v-row>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import Carousel from "@/components/Carousel.vue";
import EventCard from "@/components/EventCard.vue";
export default {
  name: "Home",
  components: {
    Carousel,
    EventCard
  },

  data() {
    return {
      events: [
        {
          id: "1 for jk",
          title: "Runup to 2023",
          desc:
            "Adeolu becomes the national Chairman of Alliance for Tech people in politics",
          author: "J-k",
          likes: 13,
          shares: 10
        },
        {
          id: "2 for deolu",
          title: "Spy Lee Relocation to Naija",
          desc:
            "Spy Lee, the Genereal Partner at SpyDeolu VC firm considering opening a Nigerian office from where he will oversee the firm's African operations ",
          author: "Adeolu",
          likes: 298,
          shares: 3
        },
        {
          id: "3 for ooaa",
          title: "#BlackLivesMatter",
          desc:
            "As Trump intensifies efforts to arrest prosestors, people no longer upload videos and photos of the protest online. No more looting recently",
          author: "Big Chief",
          likes: 41,
          shares: 56
        }
      ]
    };
  }
};
</script>

<style scoped></style>

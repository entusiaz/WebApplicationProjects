<template>
  <div>
    <EventCard :event="event" />

    <!-- <h1>this is a timeline of selected {{ $route.params.id }} event</h1> -->
    <TimelineItem
      v-for="timeline in timelines"
      :key="timeline.id"
      :timeline="timeline"
    />
  </div>
</template>

<script>
//import TimelineItem from "@/components/TimelineItem.vue";
import EventCard from "@/components/EventCard.vue";
import TimelineItem from "@/components/TimelineItem.vue";
export default {
  name: "EventTimeline",
  components: {
    EventCard,
    TimelineItem
  },
  props: {
    id: String,
    event: Object
  },

  data() {
    return {
      timelines: [
        {
          id: "1 for jk",
          title: this.event.title,
          desc:
            "Adeolu becomes the national Chairman of Alliance for Tech people in politics",
          author: this.event.author,
          likes: 13,
          shares: 10
        },
        {
          id: "2 for deolu",
          title: this.event.title,
          desc:
            "Spy Lee, the Genereal Partner at SpyDeolu VC firm considering opening a Nigerian office from where he will oversee the firm's African operations ",
          author: this.event.author,
          likes: 298,
          shares: 3
        },
        {
          id: "3 for ooaa",
          title: this.event.title,
          desc:
            "As Trump intensifies efforts to arrest prosestors, people no longer upload videos and photos of the protest online. No more looting recently",
          author: this.event.author,
          likes: 41,
          shares: 56
        }
      ]
    };
  }
};
</script>

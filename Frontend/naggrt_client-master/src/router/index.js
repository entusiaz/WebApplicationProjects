import Vue from "vue";
import VueRouter from "vue-router";
import EventList from "../views/EventList.vue";
import EventTimeline from "../views/EventTimeline.vue";
import PosterAccount from "../views/PosterAccount.vue";
// import NotFoundPage from "../components/NotFoundPage.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "event-list",
    component: EventList
  },
  {
    path: "/event/:id",
    name: "event-timeline",
    component: EventTimeline,
    props: true
  },
  {
    path: "/account/:id",
    name: "poster-account",
    component: PosterAccount,
    props: true
  }
  // {
  //   path: "*",
  //   component: NotFoundPage,
  // },
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;

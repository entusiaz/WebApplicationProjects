<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <router-link :to="{ name: 'event-timeline', params: { id }}">
          <!-- <router-link :to="{ name: 'booking', params: { courseRecommended }}"> -->

          <v-card
            v-for="(event, index) in events"
            :key="index"
            class="mb-4 mx-auto"
            width="400"
            outlined
          >
            <v-card-title>
              <div class="text-left">
                <v-icon small left>mdi-twitter</v-icon>
                <span
                  class="font-weight-regular text-left"
                  style="max-width: 270px; font-size: 16px; "
                >{{ event.title }}</span>
              </div>
            </v-card-title>
            <!--  </v-card-title> -->
            <span></span>
            <span
              class="d-inline-block font-weight-light text-left"
              style="max-width: 270px; font-size: 14px; margin-left: 5%"
            >{{ event.desc }}</span>

            <v-card-actions>
              <v-list-item class="grow">
                <v-list-item-avatar color="grey darken-3">
                  <v-img
                    class="elevation-6 small"
                    src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
                  ></v-img>
                </v-list-item-avatar>

                <v-list-item-content>
                  <v-list-item-title>{{ event.author }}</v-list-item-title>
                </v-list-item-content>

                <v-row align="center" justify="end">
                  <v-icon class="small mr-1">mdi-heart</v-icon>
                  <span class="subheading mr-2">{{ event.likes }}</span>
                  <span class="mr-1">·</span>
                  <v-icon class="small mr-1">mdi-share-variant</v-icon>
                  <span class="subheading">{{ event.shares }}</span>
                </v-row>
              </v-list-item>
            </v-card-actions>
          </v-card>
        </router-link>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",

  data: () => ({
    events: [
      {
        title: "Runup to 2023",
        desc:
          "Adeolu becomes the national Chairman of Alliance for Tech people in politics",
        author: "J-k",
        likes: 13,
        shares: 10
      },
      {
        title: "Spy Lee Relocation to Naija",
        desc:
          "Spy Lee, the Genereal Partner at SpyDeolu VC firm considering opening a Nigerian office from where he will oversee the firm's African operations ",
        author: "Adeolu",
        likes: 298,
        shares: 3
      },
      {
        title: "#BlackLivesMatter",
        desc:
          "As Trump intensifies efforts to arrest prosestors, people no longer upload videos and photos of the protest online. No more looting recently",
        author: "Big Chief",
        likes: 41,
        shares: 56
      }
    ]
  })
};
</script>

<template>
  <v-container fluid>
    <!-- 
    <v-row justify="center">
      <v-subheader>My Account</v-subheader>

      <v-expansion-panels popout>
        <v-expansion-panel
          v-for="(message, i) in messages"
          :key="i"
          hide-actions
        >
          <v-expansion-panel-header>
            <v-row
              align="center"
              class="spacer"
              no-gutters
            >
              <v-col
                cols="4"
                sm="2"
                md="1"
              >
                <v-avatar
                  size="36px"
                >
                  <img
                    v-if="message.avatar"
                    alt="Avatar"
                    src="https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"
                  >
                  <v-icon
                    v-else
                    :color="message.color"
                    v-text="message.icon"
                  ></v-icon>
                </v-avatar>
              </v-col>

              <v-col
                class="hidden-xs-only"
                sm="5"
                md="3"
              >
                <strong v-html="message.name"></strong>
                <span
                  v-if="message.total"
                  class="grey--text"
                >
                  &nbsp;({{ message.total }})
                </span>
              </v-col>

              <v-col
                class="text-no-wrap"
                cols="5"
                sm="3"
              >
                <v-chip
                  v-if="message.new"
                  :color="`${message.color} lighten-4`"
                  class="ml-0 mr-2 black--text"
                  label
                  small
                >
                  {{ message.new }} new
                </v-chip>
                <strong v-html="message.title"></strong>
              </v-col>

              <v-col
                v-if="message.excerpt"
                class="grey--text text-truncate hidden-sm-and-down"
              >
                &mdash;
                {{ message.excerpt }}
              </v-col>
            </v-row>
          </v-expansion-panel-header>

          <v-expansion-panel-content>
            <v-divider></v-divider>
            <v-card-text v-text="lorem"></v-card-text>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-row>-->

    <!-- <v-row align="center" justify="center" class="account-nav">My Events</v-row> -->
    <v-row>
      <v-col>
        <router-link :to="{ name: 'event-list' }">
          <v-button>My Events</v-button>
        </router-link>
      </v-col>
      <v-col>
        <v-avatar>
          <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
        </v-avatar>
      </v-col>
    </v-row>

    <v-row align="center" justify="center" class="mb-n4">
      <v-col b-n2 cols="12" sm="6">
        <v-textarea
          label="Add an event"
          auto-grow
          outlined
          rows="3"
          row-height="25"
          class="mb-n6"
          shaped
        ></v-textarea>
      </v-col>
    </v-row>

    <!-- <div class="form-group" v-for="(input,k) in inputs" :key="k">
      <input type="text" class="form-control" v-model="input.name" />
      <span>
        <i class="fas fa-minus-circle" @click="remove(k)" v-show="k || ( !k && inputs.length > 1)"></i>
        <i class="fas fa-plus-circle" @click="add(k)" v-show="k == inputs.length-1"></i>
      </span>
    </div>-->

    <v-row
      v-for="(input, k) in inputs"
      :key="k"
      align="center"
      justify="center"
    >
      <v-col cols="10" sm="6">
        <v-textarea
          v-model="input.story"
          label="Timeline item"
          auto-grow
          outlined
          rows="1"
          row-height="25"
        ></v-textarea>
      </v-col>
      <v-col cols="2">
        <v-btn
          @click="add(k)"
          v-show="k == inputs.length - 1"
          class="mb-20"
          align="center"
          justify="center"
          small
          fab
          dark
          color="indigo"
        >
          <v-icon dark>mdi-plus</v-icon>
        </v-btn>
        <v-btn
          @click="remove(k)"
          v-show="k || (!k && inputs.length > 1)"
          class="mb-20"
          align="center"
          justify="center"
          small
          fab
          dark
          color="indigo"
        >
          <v-icon dark>mdi-minus</v-icon>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      inputs: [
        {
          story: ""
        }
      ]
      //   messages: [
      //     {
      //       avatar: 'https://avatars0.githubusercontent.com/u/9064066?v=4&s=460',
      //       name: 'John Leider',
      //       title: 'Welcome to Vuetify.js!',
      //       excerpt: 'Thank you for joining our community...',
      //     },
      //     {
      //       color: 'red',
      //       icon: 'people',
      //       name: 'Social',
      //       new: 1,
      //       total: 3,
      //       title: 'Twitter',
      //     },
      //     {
      //       color: 'teal',
      //       icon: 'local_offer',
      //       name: 'Promos',
      //       new: 2,
      //       total: 4,
      //       title: 'Shop your way',
      //       exceprt: 'New deals available, Join Today',
      //     }
      //   ]
      //lorem: 'Lorem ipsum dolor sit amet, at aliquam vivendum vel, everti delicatissimi cu eos. Dico iuvaret debitis mel an, et cum zril menandri. Eum in consul legimus accusam. Ea dico abhorreant duo, quo illum minimum incorrupte no, nostro voluptaria sea eu. Suas eligendi ius at, at nemore equidem est. Sed in error hendrerit, in consul constituam cum.',
    };
  },

  methods: {
    add() {
      this.inputs.push({ story: " " });
    },
    remove(index) {
      this.inputs.splice(index, 1);
    }
  }
};
</script>

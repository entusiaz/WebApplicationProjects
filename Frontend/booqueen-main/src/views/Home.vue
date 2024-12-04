<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-menu offset-y>
        <template v-slot:activator="{ attrs, on }">
          <v-btn
            color="primary"
            class="white--text ma-5"
            v-bind="attrs"
            v-on="on"
          >
            Select Medical Specialization
          </v-btn>
        </template>

        <v-list>
          <v-list-item v-for="speciality in specialitys" :key="speciality.id" link>
            <v-list-item-title
              v-text="speciality.title"
              v-on:click="selectedSpeciality = speciality"
            ></v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-row>

    <v-row align="center" justify="center">
      <v-menu  offset-y>
        <template v-slot:activator="{ attrs, on }">
          <v-btn
            color="primary"
            class="white--text ma-5"
            v-bind="attrs"
            v-on="on"
          >
            Select Doctor
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="doctor in selectedSpeciality.doctors"
            :key="doctor.id"
            link
          >
            <v-list-item-title
              v-text="doctor.name"
              v-on:click="selectedDoctor = doctor.id"
            ></v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-row>

    <v-row justify="center">
      <v-date-picker
        v-model="appointmentDetails.scheduledDate"
        :min="nowDate"
        @click:date="handleDateClick"
      ></v-date-picker>
    </v-row>

    <v-card flat>
      <v-card-text>
        <v-container fluid>
          <v-row>
            <v-col cols="6" sm="3" md="3">
              <v-checkbox
                v-model="chosenTime"
                label="9am-10am"
                color="red"
                value="9am-10am"
                hide-details
                @change="check"
              ></v-checkbox>
              <v-checkbox
                v-model="chosenTime"
                label="10am-11am"
                color="red darken-3"
                value="10am-11am"
                hide-details
                @change="check"
              ></v-checkbox>
            </v-col>
            <v-col cols="6" sm="3" md="3">
              <v-checkbox
                v-model="chosenTime"
                label="11am-12noon"
                color="indigo"
                value="11am-12noon"
                hide-details
                @change="check"
              ></v-checkbox>
              <v-checkbox
                v-model="chosenTime"
                label="12noon-1pm"
                color="indigo darken-3"
                value="12noon-1pm"
                hide-details
                @change="check"
              ></v-checkbox>
            </v-col>
            <v-col cols="6" sm="3" md="3">
              <v-checkbox
                v-model="chosenTime"
                label="1pm-2pm"
                color="orange"
                value="1pm-2pm"
                hide-details
                @change="check"
              ></v-checkbox>
              <v-checkbox
                v-model="chosenTime"
                label="2pm-3pm"
                color="violet"
                value="2pm-3pm"
                hide-details
                @change="check"
              ></v-checkbox>
            </v-col>
            <v-col cols="6" sm="3" md="3">
              <v-checkbox
                v-model="chosenTime"
                label="3pm-4pm"
                color="orange"
                value="3pm-4pm"
                hide-details
                @change="check"
              ></v-checkbox>
            </v-col> 
          </v-row>
        </v-container>
      </v-card-text>
    </v-card>

    <v-row align="center" justify="center" class="text-center mb-24">
      <v-btn color="primary" @click="confirmDetails"> Confirm Appointment </v-btn>
    </v-row>

    <v-row class="text-center mb-24" justify="center">
      <v-alert  v-if="showSuccess" dismissible dense text type="success" justify="space-around">
        Great! A doctor is available for your apointment
      </v-alert>
    </v-row>

    <v-row align="center" justify="center" class="text-center">
      <v-alert v-if="showFailure" dismissible dense text type="warning">
        Oops! The doctor is unavailable for the chosen period, kindly book another session.
      </v-alert>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {

  data: () => ({
    color: ["primary"],
    specialitys: null,
    selectedSpeciality: 0,
    selectedDoctor: "",
    scheduledDate: null,
    nowDate: new Date().toISOString().slice(0, 10),
    chosenTime: null,

    appointmentDetails: Object,

    status: null,
    error: null
  }),


  created() {
    axios.get("http://127.0.0.1:8000/speciality/").then((response) => {
      this.specialitys = response.data;
    });
    axios.get("http://127.0.0.1:8000/doctors/").then((response) => {
      this.doctors = response.data;                                                                                                                                                                                   
    });
  },

  computed: {
    showSuccess() {
      return this.status == 201;
    },
    showFailure() {
      return this.error;
    }

  },

  methods: {
    handleDateClick(scheduledDate) {
      if (!scheduledDate) return null
      const [year, month, day] = scheduledDate.split('-')
      this.selectedDate = `${year}-${month}-${day}`
    },
   
    check (e) {
      this.$nextTick(() => {
        console.log("time chosen is: " + this.chosenTime, e)
      })
    },

    confirmDetails() {
      this.appointmentDetails = {
        doctor: this.selectedDoctor,
        schedule_date: this.selectedDate,
        time_selected: this.chosenTime
      }
      axios
        .post(
          'http://127.0.0.1:8000/appointments/',
          this.appointmentDetails
        )
        .then((response) =>  {
          this.status = response.status
          console.log(this.status)
          this.$router.push('/');
          // window.location.reload();
        })
        .catch((error) => {
          this.error = error
          console.log(error)
          this.$router.push('/');
        })
    },
  }
};
</script> 
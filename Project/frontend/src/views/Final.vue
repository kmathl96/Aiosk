<template>
  <div class="final">
    <div class="col" style="padding-top: 600px;">
      <!-- <font-awesome-icon icon="coffee" style="font-size:10em; margin-top:250px; margin-bottom:10px;"/> -->
      <img
        src="@/assets/img/final.png"
        width="400px"
      />
      <div class="row" style="display:flex; justify-content:center; margin:10px;">
        <v-progress-circular
          :size="50"
          v-if="isLoading"
          indeterminate
          color="primary"
        ></v-progress-circular>
      </div>
      <v-btn
        height="80px"
        type="button"
        v-if="end"
        style="width:300px; font-size:2rem;"
        dark
        color="brown"
        @click="goTobase"
      >
      메인 화면으로
      </v-btn>
      <p style="margin-top:20px; margin-bottom:430px;font-size:50px;">주문이  <b>완료</b>되었습니다.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
name: "Final",
  components: {},
  data() {
        return {
            dot1:false,
            dot2:false,
            dot3:false,
            dot4:false,
            dot5:false,
            isLoading:true,
            end:false,
            class5: ['01031172353', '01075339406', '01097017106', '01043231595', '01079996903', '01022606785', '01072411120',
                    '01027176000', '01068864611', '01036908169', '01027109593', '01024772890', '01046309170', '01099207576',
                    '01050025260', '01038796220', '01086656223', '01048846650', '01099242161', '01037880179', '01020875832',
                    '01050455464'
            ],
            phone_num: ''
        }
    },
  methods: {
    goTobase() {
      this.timecheck = true;
      this.$router.push({ path: "/" });
    }
  },
  created () {
      setTimeout(()=>{this.isLoading = false, this.end = true},3000);
      this.phone_num = this.$store.getters.getPhoneNumber
  },
  watch: {
    end() {
      if (this.class5.indexOf(this.phone_num) !== -1 ) {
        axios.post(this.$SERVER_URL+"accounts/class5/", { phone_num: this.phone_num })
          .then(res => {
            console.log(res)
            this.$store.commit('setLetter', res.data['letter'])
            this.$router.push({ path: "Class" })
          })
          .catch(err => {
            console.error(err)
          })
      }
      else {
        this.$store.commit('reset');
        this.$router.push({ path: "/" })
      }
    }
  }
};
</script>


<style>
@import url(//spoqa.github.io/spoqa-han-sans/css/SpoqaHanSans-kr.css);
.final {
  background-color: white;
  font-family: 'Spoqa Han Sans', 'Spoqa Han Sans JP', 'Sans-serif';
  min-height: 1800px;
  color:#424242;
}
.active{
    color:white;
    border-color:#2c3e50;
}
</style>

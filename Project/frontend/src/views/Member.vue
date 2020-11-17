<template>
  <div class="about">
    <div style="padding-top: 100px; ">
      <div style="display:flex; justify-content:flex-end; margin-right:50px;">
      <v-dialog
      v-model="seniormodal"
      max-width="1500"
    >
      <template 
        v-slot:activator="{ on, attrs }"
      >
        <v-btn
          dark
          v-bind="attrs"
          v-on="on"
          style="width:200px; height:100px; font-size:2.2em; border-radius:0.7em; background-color:indianred;"
          @click="yessenior"
        >
          도움말
        </v-btn>
      </template>
      <v-card style="border-radius:1em;">
        <h1 style="padding-top:20px; margin-bottom:30px; font-size:3em;">
          도움말
        </h1>
        <div class="col" >
          <h3 class="text-center" style="font-size:2.0em; margin-bottom:30px;"><span style="color:deeppink;">분홍색 숫자 버튼</span>을 눌러 핸드폰 번호를 입력하시고 쿠폰 적립하세요!</h3>  
          <h3 class="text-center" style="font-size:2.0em; ">입력을 원하지 않으면 <span style="color:midnightblue;">건너뛰기 버튼</span>을 눌러주세요!</h3>
        </div>
        <div style="display:flex; justify-content:center; padding-bottom:30px; margin-top:30px;">
        <v-btn style="font-size:2em;" color="red darken-1" text @click="seniormodal = false">닫기</v-btn>
        </div>
      </v-card>
    </v-dialog>
    </div>
      <h1 style="font-size: 3em; margin-top: 150px; margin-bottom:50px;">핸드폰 번호 입력</h1>
      <font-awesome-icon icon="ticket-alt" label="쿠폰" style="font-size:10em; margin-bottom:50px;"/>
      <h3 style="margin-bottom:50px;">쿠폰 적립과 데이터 분석을 위해 전화번호를 입력해 주세요.</h3>
      <div style="display:flex; justify-content:center; padding:30px;">
        <button class="button" style="width: 500px; height:100px">
            <input placeholder="전화번호 입력" type="text" v-model="phonenum" style=" padding-left:40px; width:100%; height:auto; color:white; font-size:1.9em;">
        </button>
      </div>
      <div class="row" style="display:flex; justify-content:center;">
        <button class="num" style="width: 300px; height:100px; margin:20px;" @click="inputbum(1)">
            <p style="color:white; margin:0px; font-size:3em;">1</p>
        </button>
        <button class="num" style="width: 300px; height:100px; margin:20px;" @click="inputbum(2)">
            <p style="color:white; margin:0px; font-size:3em;">2</p>
        </button>
        <button class="num" style="width: 300px; height:100px; margin:20px;" @click="inputbum(3)">
            <p style="color:white; margin:0px; font-size:3em;">3</p>
        </button>
        </div>
        <div class="row" style="display:flex; justify-content:center;">
        <button class="num" style="width: 300px; height:100px; margin:20px;" @click="inputbum(4)">
            <p style="color:white; margin:0px; font-size:3em;">4</p>
        </button>
        <button class="num" style="width: 300px; height:100px; margin:20px;" @click="inputbum(5)">
            <p style="color:white; margin:0px; font-size:3em;">5</p>
        </button>
        <button class="num" style="width: 300px; height:100px; margin:20px;" @click="inputbum(6)">
            <p style="color:white; margin:0px; font-size:3em;">6</p>
        </button>
        </div>
        <div class="row" style="display:flex; justify-content:center;">
        <button class="num" style="width: 300px; height:100px; margin:20px;" @click="inputbum(7)">
            <p style="color:white; margin:0px; font-size:3em;">7</p>
        </button>
        <button class="num" style="width: 300px; height:100px; margin:20px;" @click="inputbum(8)">
            <p style="color:white; margin:0px; font-size:3em;">8</p>
        </button>
        <button class="num" style="width: 300px; height:100px; margin:20px;" @click="inputbum(9)">
            <p style="color:white; margin:0px; font-size:3em;">9</p>
        </button>
        </div>
        <div class="row" style="display:flex; justify-content:center;">
        <button class="num" style="width: 300px; height:100px; margin:20px;" @click="inputbum('reset')">
            <p style="color:white; margin:0px; font-size:3em;">초기화</p>
        </button>
        <button class="num" style="width: 300px; height:100px; margin:20px;" @click="inputbum(0)">
            <p style="color:white; margin:0px; font-size:3em;">0</p>
        </button>
        <button class="num" style="width: 300px; height:100px; margin:20px;" @click="inputbum('deletenum')">
            <font-awesome-icon icon="backspace" label="지우기" style="font-size:5em;"/>
        </button>
        </div>

        <div class="row" style="display:flex; justify-content:center; margin-top:50px; padding-bottom:30px;">
            <button class="button" style="width:400px; height:100px; margin:20px;" @click="nextpage('no')">
                <p style="margin:0px; font-size:1.8em">건너뛰기</p>
            </button>
            <button class="button" style="width:400px; height:100px; margin:20px;" @click="nextpage('yes')">
                <p style="margin:0px; font-size:1.8em">적립하기</p>
            </button>
        </div>
    </div>
  </div>
</template>

<script>
export default {
name: "Member",
  components: {},
  data () {
      return {
        phonenum: '010 - ',
        seniormodal: false,
      }
  },
  created() {
    this.senior=this.$store.getters.getSenior;
    if (this.senior == true){
      this.seniormodal = true
    }
    else {
      this.seniormodal = false
    }
  },
  methods: {
    yessenior(){
      this.seniormodal = true;
    },
    inputbum(num){
      if (typeof num == "number") {
          if (this.phonenum.length == 10) {
              this.phonenum += " - "
          }
          else if (this.phonenum.length >= 17) {
              return
          }
          this.phonenum += String(num)
          return
      }
      else if (num === "reset") {
          this.phonenum = "010 - "
          return
      }
      else {
          if (this.phonenum.length == 14) {
              this.phonenum = this.phonenum.substring(0,10)
              return
          }
          else if (this.phonenum.length > 6) {
            this.phonenum = this.phonenum.substring(0,this.phonenum.length-1)
            return
          }
      }
    },
    nextpage(dap){
        if (dap == 'no'){
            this.$router.push({path:'Take'})
        }
        else {
          if (this.phonenum == "010 - "){
            alert("핸드폰 번호를 입력하지 않았습니다.")
          }
          else {
            this.$store.commit('setPhoneNumber', this.phonenum);
            this.$router.push({path:'Take'})
          }
        }
    }
  },
};
</script>


<style>
.about {
  background-color: white;
  min-height: 1800px;
  color: #2c3e50;
}
.button {
  background-color:#2c3e50;
  color:white;    
  border-radius:20px;
}
input::placeholder{
  color:white;
}
.num{
  background-color:pink;
  color:white;    
  border-radius:20px;
}
</style>

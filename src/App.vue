<template>   <!--This template is what is injected into index.html-->
  <h1>{{title}}</h1>
  <h3>Upload a .jpg file of a cat or a dog</h3>
  <div class="hello">
    <input type="file" @change="onFileSelected">
  </div>
  <h3>{{feedback}}</h3>
</template>

<script>



export default {
  name: 'App',
  data() {
    return {
      selectedFile: null,
      title: "Cats and Dogs",
      feedback: ""
    }
  },
  methods: {
    onFileSelected(event) {
      const acceptedImageTypes = ['image/jpeg'];
      if (event.target.files[0] && acceptedImageTypes.includes(event.target.files[0]['type'])) {
        this.selectedFile = event.target.files[0]

        this.runningPython()
      }
      else {
        this.feedback = "wrong file type, try again"
        
      }
      
    },
    runningPython() {
      var spawner = require('child_process').spawn;
      const data_to_pass_in = {
        data_sent: 'Send this to python script',
        data_returned: undefined,};

      console.log('Data sent to python script:', data_to_pass_in);
      
      var python_process = spawner('python', ['./testpython.py', JSON.stringify(data_to_pass_in)]);

      python_process.stdout.on('data', (data) => {
        console.log('Data recieved from python script', JSON.parse(data.toString()));
      });

    }
  }
}

</script>

<!--this style pertains to the template in question-->
<style> 
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #245280;
  margin-top: 60px;
}
h1 {
  border-bottom: 0px solid rgb(248, 41, 41);
  display:inline-block;
}
</style>




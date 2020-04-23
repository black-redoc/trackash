import Vue from "vue";

const frmImg = () => {
  new Vue({
    el: "#AppfrmImg",
    data: {
      fexplorer: document.getElementById("fileExplorer"),
      csrf_token: document.getElementsByName("csrfmiddlewaretoken"),
      imgPath: `http://${window.location.host}/api/profile/`,
    },
    methods: {
      imsubmit(e) {
        e.preventDefault();
        this.fexplorer.click();
      },
      fExplorerOnChange() {
        const self = this;
        this.fexplorer.onchange = function () {
          const file = this.files[0];

          if (file) {
            const reader = new FileReader();
            reader.onload = function () {
              document.getElementById("profile-img").src = this.result;

              fetch(`${self.imgPath}update/1/`, {
                method: "PUT",
                headers: {
                  "Content-Type": "application/json",
                  "X-CSRFToken": self.csrf_token[0].value,
                },
                body: JSON.stringify({
                  image_profile: this.result,
                }),
              })
                .then((res) => {
                  console.log(res);
                  res.json();
                })
                .then();
            };

            reader.readAsDataURL(file);
          }
        };
      },
    },
    mounted() {
      this.fExplorerOnChange();
    },
  });
};

export default frmImg;

import Vue from "vue";

const frmImg = () => {
  new Vue({
    el: "#AppfrmImg",
    data: {
      fexplorer: document.getElementById("fileExplorer"),
      csrf_token: document.getElementsByName("csrfmiddlewaretoken"),
      imgPath: "http://localhost:8000/api/profile/",
      profile: {
        img:
          "https://images.unsplash.com/photo-1513789181297-6f2ec112c0bc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
      },
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
              console.log(self.profile.img);
              self.profile.img = this.result;

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
                .then(console.log);
            };

            reader.readAsDataURL(file);
          }
        };
      },
      loadImage() {
        fetch(`${this.imgPath}1/`)
          .then((res) => res.json())
          .then((data) => {
            if (data.image_profile) this.profile.img = data.image_profile;
          });
      },
    },
    created() {
      this.loadImage();
    },
    mounted() {
      this.fExplorerOnChange();
    },
  });
};

export default frmImg;

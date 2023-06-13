let app = Vue.createApp({
    data: function() {
        return {
            greeting: "Hello, World!",
            visible: false,
            showBtnText: "Show Box"
        }
    },
    methods: {
        toggleBox() {
            this.visible = !this.visible;
            if (this.visible)
                this.showBtnText = "Hide Box";
            else
                this.showBtnText = "Show Box";
        },
        greet() {
            this.greeting = "Hello!";
        }
    }
});

app.mount("#app");
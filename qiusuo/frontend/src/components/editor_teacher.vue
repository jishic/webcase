<template>
    <div>
        <editor v-model="content" @init="editorInit" lang="html" theme="monokai" width="800" height="600" @keyup.native="send($event)"></editor>
    </div>
</template>

<script>
export default{
    components: {
        editor: require('vue2-ace-editor')
    },
    data() {
        return {
            content:""
        }
    },
    created() {
        var signal = Signal("e0c9a73631634507b07b18b5263d129f");
        var session = signal.login("wwk1", "_no_need_token");
        var vm = this;
        session.onLoginSuccess = function(uid){
            vm.channel = session.channelJoin("111");
            channel.onChannelJoined = function(){
                channel.messageChannelSend(vm.content);
            };
        };
    },
    methods: {
        editorInit: function () {
            require('../../node_modules/brace/mode/html')
            require('../../node_modules/brace/mode/javascript')
            require('../../node_modules/brace/mode/less')
            require('../../node_modules/brace/theme/monokai')
        },
        send(e){
            this.channel.messageChannelSend(this.content);
        },
    }
}
</script>

<style scoped>

</style>

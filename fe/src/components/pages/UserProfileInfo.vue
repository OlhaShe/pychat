<template>
  <form class="holder" method="post" @submit.prevent="save">
      <table>
        <tbody>
        <tr>
          <th>Username:</th>
          <td><input maxlength="30" class="input" v-model="model.user" type="text"></td>
        </tr>
        <tr>
          <th>Name:</th>
          <td><input maxlength="30" class="input" v-model="model.name" type="text"></td>
        </tr>
        <tr>
          <th>City:</th>
          <td><input maxlength="50" class="input" v-model="model.city" type="text"></td>
        </tr>
        <tr>
          <th>Surname</th>
          <td><input maxlength="30" class="input" v-model="model.surname" type="text"></td>
        </tr>
        <tr>
          <th>Email:</th>
          <td><input maxlength="190" class="input" v-model="model.email" type="email"></td>
        </tr>
        <tr>
          <th>Birthday</th>
          <td><app-input-date input-class-datepicker="input-date" input-class="input" v-model="model.birthday"/></td>
        </tr>
        <tr>
          <th>Contacts:</th>
          <td><input maxlength="100" class="input" v-model="model.contacts" type="text"></td>
        </tr>
        <tr>
          <th>Sex:</th>
          <td><select  class="input" v-model="model.sex">
            <option :value="s" v-for="s in sex" >{{s}}</option>
          </select></td>
        </tr>
        <tr>
          <td colspan="2">
            <app-submit class="green-btn" value="Save Profile" :running="running"/>
          </td>
        </tr>
        </tbody>
      </table>
  </form>
</template>
<script lang="ts">
  import {State, Action, Mutation} from "vuex-class";
  import {Component, Prop, Vue} from "vue-property-decorator";
  import AppSubmit from '../ui/AppSubmit';
  import {CurrentUserInfoModel, SexModel} from "../../types/model";
  import {UserProfileDto} from '../../types/dto';
  import {currentUserInfoModelToDto, userSettingsDtoToModel} from "../../types/converters";
  import AppInputDate from '../ui/AppInputDate';
  @Component({
    components: {AppInputDate, AppSubmit}
  })
  export default class UserProfileInfo extends Vue {
    running: boolean = false;
    @State userInfo: CurrentUserInfoModel;
    model: UserProfileDto = null;

    sex = SexModel;
    @Action growlError;
    @Action growlSuccess;
    @Mutation setActiveUserId: SingleParamCB<number>;

    created() {
      this.setActiveUserId(null);
      this.model = currentUserInfoModelToDto(this.userInfo);
    }


    save() {
      this.running = true;
      this.logger.debug("Saving userProfile")();
      let cui: UserProfileDto = {...this.model};
      this.$ws.saveUser(cui, e => {
        this.running = false;
        if (e && e.action == 'setUserProfile') {
          this.growlSuccess("User profile has been saved");
        }
      })
    }
  }
</script>

<style lang="sass" scoped>
  .holder /deep/ .input.input-date
    width: 100%
</style>
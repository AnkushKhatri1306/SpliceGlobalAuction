import { Component, OnInit } from '@angular/core';
import { AuthService } from '../__services/auth.service';
import { Router } from "@angular/router";

@Component({
  selector: 'app-authentication',
  templateUrl: './authentication.component.html',
  styleUrls: ['./authentication.component.css']
})
export class AuthenticationComponent implements OnInit {
    user: object = {};
    isLogin: Boolean = true;
    registerData: object = {
      'country': 'default',
      "userType": '1'

    };
    isUnauthorized: Boolean = false;
    loginErrorMsg: string = 'Username or Password is invalid .';

  constructor(private authService: AuthService, private route: Router) { }

  ngOnInit(): void {
  }

  /* register start here */

  signUp() {
    this.authService.registerService(this.registerData).subscribe(resp => {
        if (resp.status) {
            console.log('Signup successfull');
            this.registerData = {
              'country': 'default',
              "userType": '1'
        
            };
            this.user = {};
            this.isLogin = true;
        }
    },
        error => {

        });
  }


  login() {
    console.log('here for login');
    this.authService.loginService(this.user).subscribe(resp => {
        console.log('user login', resp);
        if (resp.access) {
            localStorage.setItem('token', resp.access);
            this.route.navigate(['home']); // navigate to other page        
        }                  
    },
        error => {
            this.isUnauthorized = true;
            console.log(error);
            
            if(error.error.detail == 'No active account found with the given credentials'){
                this.loginErrorMsg = 'No account with this email .';
            }
        });
  }

  setVendorData(vendor){
    this.registerData['userType'] = vendor;
  }

}

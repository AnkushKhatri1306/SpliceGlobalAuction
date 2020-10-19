import { Component, OnInit } from '@angular/core';
import { AuthService } from '../__services/auth.service';
import { Router } from "@angular/router";



@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  userData: any = {};

  constructor(private authService: AuthService, private route: Router) { }

  ngOnInit(): void {
    this.getUserDetail();
  }

  getUserDetail() {
    let token = localStorage.getItem('token');
    this.authService.getUserDetailService(token).subscribe(resp => {
        if (resp.status == 'success') {
            this.userData = resp.data;
        }
    },
        error => {
            console.log('error');
            this.route.navigate(['login']);
            
        });
  }

  logout(){
    localStorage.clear();
    this.route.navigate(['login']);       
  }

}

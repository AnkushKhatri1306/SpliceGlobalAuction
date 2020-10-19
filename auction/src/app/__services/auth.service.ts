import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  baseUrl: string = "http://127.0.0.1:9001";
  constructor(private http: HttpClient) { }

  registerService(userData: any) {
    return this.http.post<any>(this.baseUrl + "/auth/register/", userData, {
    }).pipe(map((resp) => {
      return resp;
    }));
  }

  loginService(userData: any) {
    return this.http.post<any>(this.baseUrl + "/token/", userData, {
    }).pipe(map((resp) => {
      return resp;
    }));
  }

  getUserDetailService(token:any){
    return this.http.get<any>(this.baseUrl + '/auth/get_user_data/', {
        headers: new HttpHeaders().append('Authorization', 'Bearer '+ token)
    }).pipe(map((resp) => {
        return resp;
    }));
  }

}

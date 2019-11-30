import { Injectable } from '@angular/core';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class AccountService {
  API_URL = 'http://127.0.0.1:8000';
  
   // the actual JWT token
   public token: string;

   // the token expiration date
   public token_expires: Date;
 
   // the username of the logged in user
   public username: string;

    // constructor(private router: Router,private http: HttpClient) {
    //   this.httpOptions = {
    //     headers: new HttpHeaders({'Content-Type': 'application/json'})
    //   };
    // }
    httpHeaders = new HttpHeaders({'Content-Type':'application/json'})
	  constructor(private http:HttpClient) { }

  login(user): Observable<any> {
    return this.http.post(this.API_URL + '/auth/',user);
  }

  // public logout() {
  //   this.token = null;
  //   this.token_expires = null;
  //   this.username = null;
  // }

}

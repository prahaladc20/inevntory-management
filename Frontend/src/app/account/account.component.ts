import { Component, OnInit } from '@angular/core';
import { AccountService } from '../account.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css'],
  providers:[AccountService]
})
export class AccountComponent implements OnInit {
  public errors: any = [];
  user;
  userName;
  constructor( private router: Router,
    private accountService: AccountService) { }

    _
  ngOnInit() {
    this.user = {
      username: '',
      password: ''
    };
  }

  login(user) {
    // alert(this.user)
    this.accountService.login(this.user).subscribe(
      data => {
        console.log('login success', data.username);
        this.userName = this.user.username
        // this.Token.handle(data.access_token);
        // this.Auth.changeAuthStatus(true);
        localStorage.setItem('token',data['token'])
        localStorage.setItem('userid',this.user.username)
        
        sessionStorage.setItem('loggedUser', this.user.username);
        this.router.navigate(['list']);
      },
      err => {
        console.error('login error', err);
        this.errors = err['error'];
      }
    );

  }

}
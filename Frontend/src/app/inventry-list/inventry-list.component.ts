import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { error } from 'util';
import { AccountService } from '../account.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-inventry-list',
  templateUrl: './inventry-list.component.html',
  styleUrls: ['./inventry-list.component.css'],
  providers: [ApiService]
})
export class InventryListComponent implements OnInit {

  inventories = [{author_id:'banna',product_id:1,product_name:"Abc"},{product_id:2,product_name:"xyz"}]
  public new_invt;
  userDisplayName = '';

  constructor(private api: ApiService,private accountService: AccountService) {
  	this.getProductes();

	   }
	userIsLogged() {
		if(localStorage.getItem('token')) {
			return true
		} else {
			return false
		}
	}

  	getProductes = () => {
  		this.api.getAllProductes().subscribe(
  			data => {
				  this.inventories = data;
				  console.log(data)
  			},
  			error => {
  				console.log(error)
  			}
  		);
	  }
	  
	createInventory = () => {
		alert("hello")
		this.api.createInventory(this.new_invt).subscribe(
			data => {
				alert(this.new_invt)
			},
		error => {
			console.log(error)
		}
		);
	}

	// logout() {
	// 	alert("ll")
	// 	this.accountService.logout();
	// 	this.router.navigate(['list']);
	//   }

  ngOnInit() {
	  this.new_invt={};
	  this.userDisplayName = sessionStorage.getItem('loggedUser');
  }

}

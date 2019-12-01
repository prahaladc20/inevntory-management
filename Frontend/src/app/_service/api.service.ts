import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Inventory} from "../inventry-list/inventory";

@Injectable({
  providedIn: 'root'
})
export class ApiService {


  API_URL = 'http://127.0.0.1:8000';
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'})

  constructor(private http: HttpClient) {
  }


  getAllProductes(): Observable<any> {
    return this.http.get(this.API_URL + '/get/',
      {headers: this.httpHeaders});
  }

  createInventory(inventoty): Observable<any> {
    const listing = {
      author: 1,
      product_name: inventoty.product_name,
      vendor: inventoty.vendor,
      mrp: inventoty.mrp,
      batch_num: inventoty.batch_num,
      batch_date: inventoty.batch_date,
      quantity: inventoty.quantity,
    //   status: inventoty.status
    }
    // alert(listing.product_name)
    return this.http.post(this.API_URL + '/get/', listing,
      {headers: this.httpHeaders});
  }

  updateInventory(inventory: Inventory): Observable<any> {
	// alert(listing.product_name)
	console.log(inventory,"UPDATE")
    return this.http.put(this.API_URL + '/get/' + inventory['product_id'] + '/',inventory,
      {headers: this.httpHeaders});
  }

  deleteInventory(inventoryId): Observable<any> {
    // alert(listing.product_name)
    return this.http.delete(this.API_URL + '/get/' + inventoryId + '/',
      {headers: this.httpHeaders});
  }


}

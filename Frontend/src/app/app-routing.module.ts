import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { InventryListComponent } from './inventry-list/inventry-list.component';
import { AccountComponent } from './account/account.component';


const routes: Routes = [
  {path:"list",component:InventryListComponent},
  {path:"",component:AccountComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

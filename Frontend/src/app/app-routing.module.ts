import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {InventryListComponent} from './inventry-list/inventry-list.component';
import {AccountComponent} from './account/account.component';

import {AuthGuardService as AuthGuard} from './auth/auth-guard.service';

const routes: Routes = [
  {path: "list", component: InventryListComponent, canActivate: [AuthGuard]},
  {path: "", component: AccountComponent},
  {path: '**', redirectTo: ''}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}

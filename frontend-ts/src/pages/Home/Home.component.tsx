import React, { FC } from 'react';
import { HomeProps } from './types';
import { BudgetTable } from '../../components/BudgetTable/BudgetTable.component';

export const Home: FC<HomeProps> = ({


}) => {


  return (
    <>
      <h1>Welcome to your homepage</h1>
      <BudgetTable/>
    </>
  )
}
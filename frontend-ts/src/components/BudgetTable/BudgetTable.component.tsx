import React, { FC } from "react";
import { BudgetTableProps } from "./types";
import Paper from "@mui/material/Paper";
import { Typography } from "@mui/material";

export const BudgetTable: FC<BudgetTableProps> = () => {
  return (
    <>
      <Paper elevation={1} style={{ padding: 20, maxWidth: 500 }}>
        <Typography variant="h6">Your Monthly Budgets</Typography>
      </Paper>
    </>
  );
};

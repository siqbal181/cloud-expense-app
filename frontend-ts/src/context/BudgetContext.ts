import React, { createContext, useReducer, ReactNode } from 'react';
import { BudgetIte}

interface BudgetsContextProps {
  state: BudgetsState;
  dispatch: React.Dispatch<BudgetsAction>;
}

const defaultValue: BudgetsContextProps = {
  state: { budgets: [] },
  dispatch: () => {},
};

export const BudgetsContext = createContext(defaultValue);

export const budgetsReducer = (state: BudgetsState, action: BudgetsAction): BudgetsState => {
  switch (action.type) {
    case 'SET_BUDGETS':
      const fetchedBudgets = action.payload.map((budget) => ({
        ...budget,
        source: 'database',
      }));
      return {
        budgets: fetchedBudgets,
      };
    case 'CREATE_BUDGET':
      const newBudgetItem = { ...action.payload, source: 'local' };
      return {
        budgets: [...state.budgets, newBudgetItem],
      };
    case 'UPDATE_BUDGET':
      const { _id, budget } = action.payload;
      const updatedBudgets = state.budgets.map((budgetItem) =>
        budgetItem._id === _id ? { ...budgetItem, budget } : budgetItem
      );
      return {
        budgets: updatedBudgets,
      };
    default:
      return state;
  }
};

export const BudgetsContextProvider: FC<{ children: ReactNode }> = ({ children }) => {
  const [state, dispatch] = useReducer(budgetsReducer, defaultValue.state);

  return (
    <BudgetsContext.Provider value={{ state, dispatch }}>
      {children}
    </BudgetsContext.Provider>
  );
};
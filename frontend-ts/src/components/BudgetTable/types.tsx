interface BudgetItem {
  _id: string;
  budget: number;
  source: 'database' | 'local';
}

interface BudgetsState {
  budgets: BudgetItem[];
}

type BudgetsAction =
  | { type: 'SET_BUDGETS'; payload: BudgetItem[] }
  | { type: 'CREATE_BUDGET'; payload: BudgetItem }
  | { type: 'UPDATE_BUDGET'; payload: { _id: string; budget: number } };
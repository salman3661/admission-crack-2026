import React from 'react';
import { ExamView } from './ExamView';

export const QuestionBankView: React.FC<React.ComponentProps<typeof ExamView>> = (props) => {
  return <ExamView {...props} />;
};

export default QuestionBankView;
export { ExamView };

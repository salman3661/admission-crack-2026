import React from 'react';
import { ExamView } from './ExamView';

export const QuestionsView: React.FC<React.ComponentProps<typeof ExamView>> = (props) => {
  return <ExamView {...props} />;
};

export default QuestionsView;
export { ExamView };

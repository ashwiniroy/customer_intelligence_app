import { Paper, Typography } from "@mui/material";
import AppInput from "../../Components/Common/Input";
import AppButton from "../../Components/Common/Button";

const AIInputPanel = () => {
  return (
    <Paper sx={{ p: 3, height: "100%" }}>
      <Typography variant="h6" mb={2}>
        Ask AI
      </Typography>

      <AppInput
        label="Ask anything about customer reviews..."
        multiline
        rows={6}
      />

      <AppButton sx={{ mt: 3 }} fullWidth>
        Ask AI
      </AppButton>
    </Paper>
  );
};

export default AIInputPanel;
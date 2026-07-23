import Grid from "@mui/material/Grid";

import DashboardHeader from "../../Components/Dashboard/DashboardHeader";
import StatCard from "../../Components/Dashboard/StatCard";
import RecentReviewCard from "../../Components/Dashboard/RecentReviewCard";

import ReviewsIcon from "@mui/icons-material/RateReview";
import ThumbUpIcon from "@mui/icons-material/ThumbUp";
import ThumbDownIcon from "@mui/icons-material/ThumbDown";
import StarIcon from "@mui/icons-material/Star";

const Dashboard = () => {
  return (
    <>
      <DashboardHeader />

      <Grid container spacing={3} mb={4}>
        <Grid size={{ xs: 12, md: 3 }}>
          <StatCard
            title="Total Reviews"
            value="1250"
            icon={<ReviewsIcon color="primary" />}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 3 }}>
          <StatCard
            title="Positive"
            value="980"
            icon={<ThumbUpIcon color="success" />}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 3 }}>
          <StatCard
            title="Negative"
            value="150"
            icon={<ThumbDownIcon color="error" />}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 3 }}>
          <StatCard
            title="Average Rating"
            value="4.6"
            icon={<StarIcon color="warning" />}
          />
        </Grid>
      </Grid>

      <DashboardHeader />

      <RecentReviewCard
        customer="Ashwini Kumar"
        title="Amazing product quality."
        rating={5}
        sentiment="Positive"
      />

      <RecentReviewCard
        customer="John Smith"
        title="Delivery was delayed."
        rating={2}
        sentiment="Negative"
      />

      <RecentReviewCard
        customer="David"
        title="Packaging was good."
        rating={4}
        sentiment="Positive"
      />
    </>
  );
};

export default Dashboard;